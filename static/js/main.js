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



/*==============AUCTION================*/
$(document).ready(function () {
    var dateCreated = document.getElementById("date_created").textContent
        var countDownDate = new Date(dateCreated).getTime();
        var expiryDate = document.getElementById("expiry-date")
        var productPrice = $("#product-price").text()
        var currentBid = $("#current-price").text()
        var buyButton = document.getElementById("purchase-button")
        var buyButtonWrapper = document.getElementById("buy-button-wrapper")
        var priceExpired = document.getElementById("price-expired")
        var submitBid = document.getElementById("place-bid")
        var winningBidAlert = document.getElementById("winning-bid-alert")
        var winningButton  = document.getElementById("bid-winning-purchase")
        var winningUser = document.getElementById("winning-user")
        var winningPrice = document.getElementById("inner-current-bid")
        var x = setInterval(function() {
            var now = new Date().getTime();
            var distance = countDownDate - now;
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);
            expiryDate.innerHTML = "Bid Expires In: " + days + "d " + hours + "h " +
                minutes + "m " + seconds + "s ";
            if (distance < 0) {
                clearInterval(x);
                expiryDate.innerHTML = "BID EXPIRED !!!";
                expiryDate.style.color = "crimson";
            }
            else if (!days){
                expiryDate.innerHTML = "Bid Expires In: " + hours + "h " +
                minutes + "m " + seconds + "s ";
                if (!days && !hours){
                    expiryDate.innerHTML = "Bid Expires In: " + minutes + "m " + seconds + "s ";
                    expiryDate.style.color = "crimson";
                }
            }
        if (productPrice - 1  < currentBid){
                buyButtonWrapper.style.display = "none"
                priceExpired.style.display = "block";
                
            }
        var last_user = $("#last-user").text();
        var expiry_date = $("#expiry-date").text();
        var currentUser = $("#current-user").text()
        if(expiry_date == "BID EXPIRED !!!"){
            priceExpired.style.display = "none"
            submitBid.parentNode.removeChild(submitBid);
            buyButtonWrapper.style.display = "none"
            winningUser.innerHTML = "The Auction was Won by | " + last_user
            winningPrice.innerHTML = "The Auction was Won at " + currentBid + "£"

            if(currentUser == last_user){
                winningBidAlert.style.display = "block"
                winningButton.style.display = "block"
                winningUser.innerHTML = "Congratulations you've WON the Auction for this item please proceed to checkout"
                
            }
        }
        });
    });
