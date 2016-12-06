function next(curp, nexp){
    document.getElementById("page" + curp).style.display = "none";
    document.getElementById("page" + nexp).style.display = "inline";
}
function previous(lastp, curp){
    document.getElementById("page" + curp).style.display = "none";
    document.getElementById("page" + lastp).style.display = "inline";
}
$(document).ready(function(){
      $('.carousel').carousel({
          time_constant:500
      });
});
autoplay();
function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 1500);
}
$(document).ready(function(){
      $('.slider').slider({
          full_width: true,
          indicators: false
        });
    });