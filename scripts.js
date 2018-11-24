function randElement(list)
{
  return list[Math.floor(Math.random() * list.length)];
}

var images = ["air.png", "blid.jpg", "down.jpg", "spray.jpg", "stuw.png", "zoink.png"];

document.getElementById("randImage").src = "shags/" + randElement(images);
