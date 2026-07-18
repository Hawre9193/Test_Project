import streamlit as st
import streamlit.components.v1 as components

# ناونیشانی بەشەکە لە سایتەکەتدا
st.title("🐍 یاری مار لەناو سایتەکەی خۆم")
st.write("بە تیری سەر کیبۆردەکە (سەرەوە، خوارەوە، ڕاست، چەپ) یاری بکە!")

# لۆجیکی یارییەکە کە لەناو سایتەکەتدا وەک پەنجەرەیەک دەکرێتەوە
snake_game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: #0e1117;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 420px;
    margin: 0;
  }
  canvas {
    background-color: #000000;
    box-shadow: 0 0 15px #00ffff;
    border: 2px solid #00ffff;
    border-radius: 10px;
  }
</style>
</head>
<body>

<canvas id="gameCanvas" width="400" height="400"></canvas>

<script>
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");

  const box = 20;
  let snake = [];
  snake[0] = { x: 9 * box, y: 10 * box };

  let food = {
    x: Math.floor(Math.random() * 19 + 1) * box,
    y: Math.floor(Math.random() * 19 + 1) * box
  };

  let score = 0;
  let d;

  document.addEventListener("keydown", direction);

  function direction(event) {
    let key = event.keyCode;
    if (key == 37 && d != "RIGHT") { d = "LEFT"; }
    else if (key == 38 && d != "DOWN") { d = "UP"; }
    else if (key == 39 && d != "LEFT") { d = "RIGHT"; }
    else if (key == 40 && d != "UP") { d = "DOWN"; }
  }

  function draw() {
    ctx.clearRect(0, 0, 400, 400);

    for (let i = 0; i < snake.length; i++) {
      ctx.fillStyle = (i == 0) ? "#00FFFF" : "#008B8B"; // ڕەنگی کرمەکە
      ctx.fillRect(snake[i].x, snake[i].y, box, box);
      ctx.strokeStyle = "black";
      ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }

    ctx.fillStyle = "#FF1493"; // ڕەنگی خواردنەکە
    ctx.fillRect(food.x, food.y, box, box);

    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if (d == "LEFT") snakeX -= box;
    if (d == "UP") snakeY -= box;
    if (d == "RIGHT") snakeX += box;
    if (d == "DOWN") snakeY += box;

    if (snakeX == food.x && snakeY == food.y) {
      score++;
      food = {
        x: Math.floor(Math.random() * 19 + 1) * box,
        y: Math.floor(Math.random() * 19 + 1) * box
      };
    } else {
      snake.pop();
    }

    let newHead = { x: snakeX, y: snakeY };

    // دۆڕاندن کاتێک بەر دیوار یان خۆی دەکەوێت
    if (snakeX < 0 || snakeX >= 400 || snakeY < 0 || snakeY >= 400 || collision(newHead, snake)) {
      clearInterval(game);
      ctx.fillStyle = "red";
      ctx.font = "30px Arial";
      ctx.fillText("SYSTEM FAILURE!", 70, 200);
    }

    snake.unshift(newHead);
  }

  function collision(head, array) {
    for (let i = 0; i < array.length; i++) {
      if (head.x == array[i].x && head.y == array[i].y) {
        return true;
      }
    }
    return false;
  }

  let game = setInterval(draw, 100); // خێرایی یارییەکە
</script>

</body>
</html>
"""

# نیشاندانی یارییەکە لەناو سایتەکەت
components.html(snake_game_html, height=450)
