import streamlit as st
import streamlit.components.v1 as components

st.title("🐍 یاری مار (بە تایبەتمەندی مۆبایل)")

snake_game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { background: #0e1117; display: flex; flex-direction: column; align-items: center; }
  canvas { background: #000; border: 2px solid #00ffff; }
  .controls { display: grid; grid-template-columns: repeat(3, 50px); gap: 10px; margin-top: 10px; }
  button { width: 50px; height: 50px; background: #00ffff; border: none; border-radius: 5px; font-weight: bold; }
</style>
</head>
<body>
<canvas id="gameCanvas" width="300" height="300"></canvas>
<div class="controls">
  <div></div><button onclick="setDir('UP')">▲</button><div></div>
  <button onclick="setDir('LEFT')">◀</button><button onclick="setDir('DOWN')">▼</button><button onclick="setDir('RIGHT')">▶</button>
</div>
<script>
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");
  const box = 20;
  let snake = [{x: 140, y: 140}];
  let food = {x: 100, y: 100};
  let d = "RIGHT";

  function setDir(newDir) { 
    if(newDir == "UP" && d != "DOWN") d = "UP";
    if(newDir == "DOWN" && d != "UP") d = "DOWN";
    if(newDir == "LEFT" && d != "RIGHT") d = "LEFT";
    if(newDir == "RIGHT" && d != "LEFT") d = "RIGHT";
  }

  function draw() {
    ctx.clearRect(0, 0, 300, 300);
    ctx.fillStyle = "#FF1493";
    ctx.fillRect(food.x, food.y, box, box);
    
    for(let i=0; i<snake.length; i++) {
      ctx.fillStyle = (i==0) ? "#00ffff" : "white";
      ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }
    
    let head = {x: snake[0].x, y: snake[0].y};
    if(d=="UP") head.y -= box;
    if(d=="DOWN") head.y += box;
    if(d=="LEFT") head.x -= box;
    if(d=="RIGHT") head.x += box;
    
    snake.unshift(head);
    snake.pop();
  }
  setInterval(draw, 150);
</script>
</body>
</html>
"""
components.html(snake_game_html, height=500)
