// Configuration
const rows = 100;
const cols = 100;
let grid = createGrid();

// Select the grid container
const gridContainer = document.querySelector('.grid');

// Create a 2D array for the grid
function createGrid() {
  return new Array(rows).fill(null).map(() => new Array(cols).fill(0));
}

// Randomly populate the grid
function randomizeGrid(grid) {
  return grid.map(row => row.map(() => Math.floor(Math.random() * 2)));
}

// Initialize the grid with DOM elements
function initializeGrid(grid) {
  gridContainer.innerHTML = ''; // Clear the grid container first

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      if (grid[row][col] === 1) {
        cell.classList.add('alive');
      }
      gridContainer.appendChild(cell);
    }
  }
}

// Update the grid based on Conway's rules
function updateGrid(grid) {
  const nextGen = createGrid();

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const neighbors = countNeighbors(grid, row, col);
      const cell = grid[row][col];

      // Apply Conway's Game of Life rules
      if (cell === 1 && (neighbors < 2 || neighbors > 3)) {
        nextGen[row][col] = 0;
      } else if (cell === 0 && neighbors === 3) {
        nextGen[row][col] = 1;
      } else {
        nextGen[row][col] = cell;
      }
    }
  }

  return nextGen;
}

// Count live neighbors of a cell
function countNeighbors(grid, x, y) {
  let sum = 0;
  for (let i = -1; i <= 1; i++) {
    for (let j = -1; j <= 1; j++) {
      if (i === 0 && j === 0) continue; // Skip the cell itself

      const row = (x + i + rows) % rows;
      const col = (y + j + cols) % cols;

      sum += grid[row][col];
    }
  }
  return sum;
}

// Render the grid on the page
function render(grid) {
  const cells = document.querySelectorAll('.cell');
  cells.forEach((cell, index) => {
    const row = Math.floor(index / cols);
    const col = index % cols;

    if (grid[row][col] === 1) {
      cell.classList.add('alive');
    } else {
      cell.classList.remove('alive');
    }
  });
}

// Main game loop
function gameLoop() {
  grid = updateGrid(grid);
  render(grid);
  requestAnimationFrame(gameLoop);
}

// Start the game
grid = randomizeGrid(grid);
initializeGrid(grid);
gameLoop();
