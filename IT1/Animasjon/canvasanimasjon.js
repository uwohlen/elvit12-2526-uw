/* Funksjon for å tegne trekanter på en canvas-tagg
  ctx - canvas.getContext("2d")-variabel
  x, y - tre posisjoner for hjørnene i trekanten
  LBredde - linjebredde
  farge - fyllfarge
  strek - strekfarge
*/
function trekant(ctx,x1,y1,x2,y2,x3,y3,LBredde=1,farge="blue",strek="black") {
  ctx.beginPath()
  ctx.lineWidth = LBredde
  ctx.fillStyle = farge
  ctx.strokeStyle = strek
  ctx.moveTo(x1,y1)
  ctx.lineTo(x2,y2)
  ctx.lineTo(x3,y3)
  ctx.closePath()
  ctx.stroke()
  ctx.fill()  
}


/* Funksjon for å tegne en stjerne
    ctx - canvas.getContext("2d")-variabel
    origox, origoy - posisjon av nedre venstre stjernespiss
    farge - stjernefarge
    faktor - relativ størrelse, tall mellom 0 og 1 (eller større...)
*/
function stjerne(ctx,origox,origoy,farge="white",faktor=1) {
  ctx.beginPath();
  ctx.fillStyle = farge;

  ctx.moveTo(origox,origoy);
  ctx.lineTo(origox+50*faktor,origoy-36*faktor);
  ctx.lineTo(origox+100*faktor,origoy);
  ctx.lineTo(origox+81*faktor,origoy-59*faktor);
  ctx.lineTo(origox+131*faktor,origoy-95*faktor);
  ctx.lineTo(origox+69*faktor,origoy-95*faktor);
  ctx.lineTo(origox+50*faktor,origoy-154*faktor);
  ctx.lineTo(origox+31*faktor,origoy-95*faktor);
  ctx.lineTo(origox-31*faktor,origoy-95*faktor);
  ctx.lineTo(origox+19*faktor,origoy-59*faktor);
  ctx.closePath();
  ctx.fill();
}
