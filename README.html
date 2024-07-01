<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">
  <style>
    .cell { fill: white; stroke: black; stroke-width: 2; }
    .x { stroke: red; stroke-width: 4; }
    .o { stroke: blue; stroke-width: 4; fill: none; }
    .win { stroke: green; stroke-width: 4; }
  </style>
  
  <!-- Game board -->
  <rect x="0" y="0" width="300" height="300" fill="#f0f0f0"/>
  <line x1="100" y1="0" x2="100" y2="300" stroke="black" stroke-width="2"/>
  <line x1="200" y1="0" x2="200" y2="300" stroke="black" stroke-width="2"/>
  <line x1="0" y1="100" x2="300" y2="100" stroke="black" stroke-width="2"/>
  <line x1="0" y1="200" x2="300" y2="200" stroke="black" stroke-width="2"/>
  
  <!-- Clickable cells -->
  <rect class="cell" x="0" y="0" width="100" height="100" onclick="play(0)"/>
  <rect class="cell" x="100" y="0" width="100" height="100" onclick="play(1)"/>
  <rect class="cell" x="200" y="0" width="100" height="100" onclick="play(2)"/>
  <rect class="cell" x="0" y="100" width="100" height="100" onclick="play(3)"/>
  <rect class="cell" x="100" y="100" width="100" height="100" onclick="play(4)"/>
  <rect class="cell" x="200" y="100" width="100" height="100" onclick="play(5)"/>
  <rect class="cell" x="0" y="200" width="100" height="100" onclick="play(6)"/>
  <rect class="cell" x="100" y="200" width="100" height="100" onclick="play(7)"/>
  <rect class="cell" x="200" y="200" width="100" height="100" onclick="play(8)"/>
  
  <!-- Game pieces (initially hidden) -->
  <g id="pieces"></g>
  
  <script type="text/javascript"><![CDATA[
    let currentPlayer = 'x';
    let gameState = ['', '', '', '', '', '', '', '', ''];
    const winCombos = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
      [0, 4, 8], [2, 4, 6] // Diagonals
    ];
    
    function play(cell) {
      if (gameState[cell] === '') {
        gameState[cell] = currentPlayer;
        drawPiece(cell);
        if (checkWin()) {
          highlightWin();
        } else if (gameState.every(cell => cell !== '')) {
          // It's a draw
        } else {
          currentPlayer = currentPlayer === 'x' ? 'o' : 'x';
        }
      }
    }
    
    function drawPiece(cell) {
      const x = (cell % 3) * 100 + 50;
      const y = Math.floor(cell / 3) * 100 + 50;
      const piece = document.createElementNS("http://www.w3.org/2000/svg", currentPlayer === 'x' ? 'g' : 'circle');
      
      if (currentPlayer === 'x') {
        const line1 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
        line1.setAttribute('x1', x - 20);
        line1.setAttribute('y1', y - 20);
        line1.setAttribute('x2', x + 20);
        line1.setAttribute('y2', y + 20);
        line1.setAttribute('class', 'x');
        piece.appendChild(line1);
        
        const line2 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
        line2.setAttribute('x1', x + 20);
        line2.setAttribute('y1', y - 20);
        line2.setAttribute('x2', x - 20);
        line2.setAttribute('y2', y + 20);
        line2.setAttribute('class', 'x');
        piece.appendChild(line2);
      } else {
        piece.setAttribute('cx', x);
        piece.setAttribute('cy', y);
        piece.setAttribute('r', 30);
        piece.setAttribute('class', 'o');
      }
      
      document.getElementById('pieces').appendChild(piece);
    }
    
    function checkWin() {
      return winCombos.some(combo => {
        return combo.every(cell => {
          return gameState[cell] === currentPlayer;
        });
      });
    }
    
    function highlightWin() {
      const winningCombo = winCombos.find(combo => {
        return combo.every(cell => {
          return gameState[cell] === currentPlayer;
        });
      });
      
      const line = document.createElementNS("http://www.w3.org/2000/svg", 'line');
      const start = winningCombo[0];
      const end = winningCombo[2];
      line.setAttribute('x1', (start % 3) * 100 + 50);
      line.setAttribute('y1', Math.floor(start / 3) * 100 + 50);
      line.setAttribute('x2', (end % 3) * 100 + 50);
      line.setAttribute('y2', Math.floor(end / 3) * 100 + 50);
      line.setAttribute('class', 'win');
      
      document.getElementById('pieces').appendChild(line);
    }
  ]]></script>
</svg>
