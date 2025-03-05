import pygame
import sys
import random
import numpy as np
from main import (
    Grid,
    Road,
    Residential,
    Store,
    Factory,
    Power,
    Water,
    Sewage,
    Waste,
    Fire,
    Police,
    Health,
    Specialization,
)

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GRID_SIZE = 12  # Size of each grid cell in pixels
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 200
BUTTON_MARGIN = 20
GRID_MARGIN = 50  # Margin around the grid

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (100, 100, 100)
RED = (220, 80, 80)
GREEN = (80, 200, 80)
BLUE = (80, 80, 220)
YELLOW = (220, 220, 80)
PURPLE = (180, 100, 220)
BROWN = (139, 69, 19)
CYAN = (80, 220, 220)
ORANGE = (255, 165, 0)
PINK = (255, 182, 193)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)
BACKGROUND = (240, 240, 245)

# Building colors and symbols
BUILDING_COLORS = {
    Road: (DARK_GRAY, "R"),
    Residential: (GREEN, "H"),
    Store: (BLUE, "S"),
    Factory: (ORANGE, "F"),
    Power: (RED, "P"),
    Water: (CYAN, "W"),
    Sewage: (BROWN, "SW"),
    Waste: (ORANGE, "WT"),
    Fire: (RED, "FD"),
    Police: (LIGHT_BLUE, "PD"),
    Health: (PINK, "H+"),
    Specialization: (PURPLE, "SP"),
}


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        color,
        hover_color,
        text_color=BLACK,
        font_size=20,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font_size = font_size
        self.is_hovered = False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color

        # Draw button with anti-aliased edges
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        pygame.draw.rect(screen, DARK_GRAY, self.rect, 2, border_radius=5)

        # Use anti-aliased font
        font = pygame.font.SysFont("Arial", self.font_size, True)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)

    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click


class Visualizer:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("SimCity Builder Visualizer")

        # Set icon
        icon = pygame.Surface((32, 32))
        icon.fill(GREEN)
        pygame.draw.rect(icon, BLUE, (0, 0, 16, 16))
        pygame.draw.rect(icon, RED, (16, 16, 16, 16))
        pygame.display.set_icon(icon)

        self.grid = Grid(50, 68)  # Using the default grid size from main.py
        self.population = 0
        self.happiness = 0

        # Create buttons
        button_y = SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN

        self.generate_button = Button(
            SCREEN_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN,
            button_y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Generate Random Layout",
            (230, 230, 230),
            (200, 200, 200),
            BLACK,
            18,
        )

        self.optimize_button = Button(
            SCREEN_WIDTH - 2 * BUTTON_WIDTH - 2 * BUTTON_MARGIN,
            button_y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Optimize Layout",
            (230, 230, 230),
            (200, 200, 200),
            BLACK,
            18,
        )

        # Generate initial random layout
        self.generate_random_layout()

    def generate_random_layout(self):
        # Clear the grid
        self.grid = Grid(50, 68)

        # Create a more structured layout
        # First, create a road network
        self._create_road_network()

        # Then place buildings in a more organized way
        self._place_buildings()

        # Calculate population
        self.calculate_population()

    def _create_road_network(self):
        # Create a grid of roads with blocks in between
        block_size = 4  # Size of blocks between roads

        # Horizontal roads
        for i in range(0, self.grid.length, block_size + 1):
            for j in range(self.grid.width):
                road = Road()
                self.grid.place_building(road, i, j)

        # Vertical roads
        for i in range(self.grid.length):
            for j in range(0, self.grid.width, block_size + 1):
                road = Road()
                self.grid.place_building(road, i, j)

    def _place_buildings(self):
        # Define building types with their parameters
        building_types = [
            (
                Residential,
                {"name": "House", "id": 1, "width": 2, "height": 2, "population": 4},
            ),
            (Store, {"name": "Store", "id": 2, "width": 3, "height": 2}),
            (
                Factory,
                {"name": "Factory", "id": 3, "width": 4, "height": 3, "pollution": 5},
            ),
            (
                Power,
                {
                    "name": "Power Plant",
                    "id": 4,
                    "width": 4,
                    "height": 4,
                    "power": 100,
                    "pollution": 10,
                },
            ),
            (
                Water,
                {"name": "Water Tower", "id": 5, "width": 2, "height": 2, "water": 50},
            ),
            (
                Fire,
                {"name": "Fire Station", "id": 6, "width": 3, "height": 2, "area": 5},
            ),
            (
                Police,
                {"name": "Police Station", "id": 7, "width": 3, "height": 2, "area": 5},
            ),
            (Health, {"name": "Hospital", "id": 8, "width": 4, "height": 3, "area": 6}),
        ]

        # Place service buildings first (fire, police, health)
        service_buildings = [building_types[5], building_types[6], building_types[7]]
        for _ in range(5):  # Place a few service buildings
            building_type, params = random.choice(service_buildings)
            building = building_type(**params)

            # Try to place it at a good location
            for _ in range(20):  # Try 20 times
                x = random.randint(0, self.grid.length - building.width)
                y = random.randint(0, self.grid.width - building.height)

                if self.grid.place_building(building, x, y):
                    break

        # Place utility buildings (power, water)
        utility_buildings = [building_types[3], building_types[4]]
        for _ in range(3):  # Place a few utility buildings
            building_type, params = random.choice(utility_buildings)
            building = building_type(**params)

            for _ in range(20):
                x = random.randint(0, self.grid.length - building.width)
                y = random.randint(0, self.grid.width - building.height)

                if self.grid.place_building(building, x, y):
                    break

        # Place residential and commercial buildings
        residential_commercial = [building_types[0], building_types[1]]
        for _ in range(100):  # Try to place many residential/commercial buildings
            building_type, params = random.choice(residential_commercial)
            building = building_type(**params)

            for _ in range(5):  # Try a few times for each building
                x = random.randint(0, self.grid.length - building.width)
                y = random.randint(0, self.grid.width - building.height)

                if self.grid.place_building(building, x, y):
                    break

        # Place some factories away from residential areas
        for _ in range(5):
            building = Factory(**building_types[2][1])

            for _ in range(10):
                x = random.randint(0, self.grid.length - building.width)
                y = random.randint(0, self.grid.width - building.height)

                if self.grid.place_building(building, x, y):
                    break

    def optimize_layout(self):
        # Simple optimization: try to add more residential buildings
        # in areas that are within service radius and not in pollution areas

        for _ in range(50):  # Try 50 times
            x = random.randint(0, self.grid.length - 2)
            y = random.randint(0, self.grid.width - 2)

            # Check if this is a good spot for a residential building
            if (
                self.grid.is_within_service_radius(x, y, 2, 2)
                and not self.grid.is_in_pollution_area(x, y, 2, 2)
                and self.grid.is_connected_to_road(x, y, 2, 2)
            ):
                # Try to place a residential building
                building = Residential("House", 1, 2, 2, 4)
                self.grid.place_building(building, x, y)

        # Recalculate population
        self.calculate_population()

    def calculate_population(self):
        total_population = 0
        total_buildings = 0

        for i in range(self.grid.length):
            for j in range(self.grid.width):
                cell = self.grid.grid[i][j]
                if isinstance(cell, Residential):
                    total_population += cell.population
                    total_buildings += 1

        self.population = total_population

        # Calculate a happiness score based on services and pollution
        happiness = 0
        if total_buildings > 0:
            service_coverage = 0
            pollution_free = 0

            for i in range(self.grid.length):
                for j in range(self.grid.width):
                    cell = self.grid.grid[i][j]
                    if isinstance(cell, Residential):
                        if self.grid.is_within_service_radius(
                            i, j, cell.width, cell.height
                        ):
                            service_coverage += 1
                        if not self.grid.is_in_pollution_area(
                            i, j, cell.width, cell.height
                        ):
                            pollution_free += 1

            if total_buildings > 0:
                happiness = (
                    (service_coverage + pollution_free) / (2 * total_buildings) * 100
                )

        self.happiness = int(happiness)

    def draw(self):
        self.screen.fill(BACKGROUND)

        # Draw grid background
        grid_width = min(self.grid.width * GRID_SIZE, SCREEN_WIDTH - 2 * GRID_MARGIN)
        grid_height = min(
            self.grid.length * GRID_SIZE,
            SCREEN_HEIGHT - 2 * GRID_MARGIN - BUTTON_HEIGHT - BUTTON_MARGIN,
        )

        grid_rect = pygame.Rect(GRID_MARGIN, GRID_MARGIN, grid_width, grid_height)
        pygame.draw.rect(self.screen, WHITE, grid_rect)
        pygame.draw.rect(self.screen, DARK_GRAY, grid_rect, 2)

        # Calculate visible area
        visible_width = min(self.grid.width, int(grid_width / GRID_SIZE))
        visible_height = min(self.grid.length, int(grid_height / GRID_SIZE))

        # Draw grid cells
        for i in range(visible_height):
            for j in range(visible_width):
                cell = self.grid.grid[i][j]
                color = WHITE
                symbol = ""

                if cell is not None:
                    for building_type, (
                        building_color,
                        building_symbol,
                    ) in BUILDING_COLORS.items():
                        if isinstance(cell, building_type):
                            color = building_color
                            symbol = building_symbol
                            break

                # Draw cell with anti-aliased border
                cell_rect = pygame.Rect(
                    GRID_MARGIN + j * GRID_SIZE,
                    GRID_MARGIN + i * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE,
                )
                pygame.draw.rect(self.screen, color, cell_rect)
                pygame.draw.rect(self.screen, (200, 200, 200), cell_rect, 1)

                # Draw symbol if not empty
                if symbol:
                    font_size = GRID_SIZE - 4
                    font = pygame.font.SysFont("Arial", font_size, True)
                    text_color = (
                        BLACK if color[0] + color[1] + color[2] > 500 else WHITE
                    )
                    text_surface = font.render(symbol, True, text_color)
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.screen.blit(text_surface, text_rect)

        # Draw buttons
        self.generate_button.draw(self.screen)
        self.optimize_button.draw(self.screen)

        # Draw stats panel
        stats_rect = pygame.Rect(
            GRID_MARGIN,
            SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN,
            SCREEN_WIDTH - 2 * BUTTON_WIDTH - 4 * BUTTON_MARGIN - GRID_MARGIN,
            BUTTON_HEIGHT,
        )
        pygame.draw.rect(self.screen, WHITE, stats_rect, border_radius=5)
        pygame.draw.rect(self.screen, DARK_GRAY, stats_rect, 2, border_radius=5)

        # Draw population and happiness
        font = pygame.font.SysFont("Arial", 18, True)
        population_text = font.render(f"Population: {self.population}", True, BLACK)
        happiness_text = font.render(f"Happiness: {self.happiness}%", True, BLACK)

        self.screen.blit(
            population_text, (stats_rect.left + 20, stats_rect.centery - 15)
        )
        self.screen.blit(happiness_text, (stats_rect.left + 20, stats_rect.centery + 5))

        # Draw legend
        legend_x = SCREEN_WIDTH - GRID_MARGIN - 150
        legend_y = GRID_MARGIN
        legend_size = 15
        legend_spacing = 25
        legend_font = pygame.font.SysFont("Arial", 14, True)

        # Draw legend title
        title_font = pygame.font.SysFont("Arial", 16, True)
        title_text = title_font.render("Building Types", True, BLACK)
        self.screen.blit(title_text, (legend_x, legend_y - 25))

        # Draw legend items
        for i, (building_type, (color, symbol)) in enumerate(BUILDING_COLORS.items()):
            pygame.draw.rect(
                self.screen,
                color,
                (legend_x, legend_y + i * legend_spacing, legend_size, legend_size),
            )
            pygame.draw.rect(
                self.screen,
                BLACK,
                (legend_x, legend_y + i * legend_spacing, legend_size, legend_size),
                1,
            )

            building_name = building_type.__name__
            text_surface = legend_font.render(building_name, True, BLACK)
            self.screen.blit(
                text_surface,
                (legend_x + legend_size + 5, legend_y + i * legend_spacing),
            )

        pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_click = True

            # Check button hover and clicks
            self.generate_button.check_hover(mouse_pos)
            self.optimize_button.check_hover(mouse_pos)

            if self.generate_button.is_clicked(mouse_pos, mouse_click):
                self.generate_random_layout()

            if self.optimize_button.is_clicked(mouse_pos, mouse_click):
                self.optimize_layout()

            self.draw()
            clock.tick(60)  # Limit to 60 FPS for smoother rendering

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    visualizer = Visualizer()
    visualizer.run()
