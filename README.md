## Hi there 👋
Get into Python

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle id="player" cx="100" cy="100" r="10" fill="blue" />
  <text id="score" x="10" y="20" font-family="Arial" font-size="16" fill="black">Score: 0</text>
  <script type="text/javascript">
    <![CDATA[
      var score = 0;
      var player = document.getElementById('player');
      var scoreText = document.getElementById('score');
      
      function movePlayer() {
        var x = Math.random() * 180 + 10;
        var y = Math.random() * 180 + 10;
        player.setAttribute('cx', x);
        player.setAttribute('cy', y);
      }
      
      function incrementScore() {
        score++;
        scoreText.textContent = 'Score: ' + score;
        movePlayer();
      }
      
      player.addEventListener('click', incrementScore);
    ]]>
  </script>
</svg>



<!--
**nathanLYJ/NathanLYJ** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
