$(document).ready(function() {
    
$( ".slide1_button" ).click(function(e) {
    goRight();
});
$( ".slide2_button" ).click(function(e) {
    goLeft();
});


function goRight(){ // inner stuff slides left
  var containerWidth = $( ".container" ).css('width').replace("px","")*1;
  var initalLeftMargin = $( ".innerLiner" ).css('margin-left').replace("px", "")*1;
    var newLeftMargin = (initalLeftMargin - containerWidth); // extra 2 for border
    $( ".innerLiner" ).animate({marginLeft: newLeftMargin}, 500);
}
function goLeft(){ // inner stuff slides right
    var containerWidth = $( ".container" ).css('width').replace("px","")*1;  
    var initalLeftMargin = $( ".innerLiner" ).css('margin-left').replace("px", "")*1;
    var newLeftMargin = (initalLeftMargin + containerWidth); // extra 2 for border
    $( ".innerLiner" ).animate({marginLeft: newLeftMargin}, 500);
}

});
