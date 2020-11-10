
function progress_bar(ratio_pos, ratio_neg) {
  console.log("ciao")
  pos_bar = document.getElementById("pos-bar")
  neg_bar = document.getElementById("neg-bar")
  pos_bar.style.width = ratio_pos
  pos_bar.innerHTML = ratio_pos
  neg_bar.style.width = ratio_neg
  neg_bar.innerHTML = ratio_neg
  document.getElementById("progress-bar").style.display = (document.getElementById("progress-bar").style.display == "none") ? "block" : "none" 
}
