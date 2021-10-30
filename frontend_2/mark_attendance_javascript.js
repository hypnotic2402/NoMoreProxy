const player = document.getElementById("player");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
const captureButton = document.getElementById("capture");
const openVideo = document.getElementById("openvijio");
let blob_image = null;
const constraints = {
  video: true,
};

captureButton.addEventListener("click", () => {
  // Draw the video frame to the canvas.
  context.drawImage(player, 0, 0, canvas.width, canvas.height);
  let file = null;
  blob_image = document.querySelector("#canvas").toBlob(function (blob_image) {
    file = new File([blob_image], "banda.png", { type: "image/png" });
  }, "image/png");
});
// Attach the video stream to the video element and autoplay.
openVideo.addEventListener("click", () => {
  navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
    player.srcObject = stream;
  });
});
closevijio.addEventListener("click", () => {
  stopvijio();
});

function DownloadCanvasAsImage() {
  let downloadLink = document.createElement("a");
  downloadLink.setAttribute("download", "maal.png");
  let canvas = document.getElementById("canvas");
  let dataURL = canvas.toDataURL("image/png");
  let url = dataURL.replace(
    /^data:image\/png/,
    "data:application/octet-stream"
  );
  downloadLink.setAttribute("href", url);
  downloadLink.click();
}
function stopvijio() {
  player.parentNode.removeChild(player);
}
