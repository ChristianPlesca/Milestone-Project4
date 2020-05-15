/*==================Profile=========*/
$(document).ready(function() {

    var readURL = function(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('.profile-pic').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $(".file-upload").on('change', function() {
        readURL(this);
    });

    $(".upload-button").on('click', function() {
        $(".file-upload").click();
    });
});

/*==================Products Headder=========*/
setTimeout(function() {
    $('#alert').fadeOut('slow');
}, 5000);


/*==================Product Details Slider=========*/

$(document).ready(function(){
    $(".fancybox").fancybox({
          openEffect: "none",
          closeEffect: "none"
      });
      
      $(".zoom").hover(function(){
          
          $(this).addClass('transition');
      }, function(){
          
          $(this).removeClass('transition');
      });
});
  

/*==============Loader================*/
$(window).on("load",function(){
    $(".loading-wrapper").fadeOut("slow");
});



/*==============Reload Page================*/
/* Reload the page after 15 seconds of inactivity */
/*
var time = new Date().getTime();
    $(document.body).bind("mousemove keypress", function(e) {
         time = new Date().getTime();
     });

     function refresh() {
         if(new Date().getTime() - time >= 60000) 
             window.location.reload(true);
         else 
             setTimeout(refresh, 15000);
     }

setTimeout(refresh, 15000);
*/