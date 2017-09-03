
$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav').addClass('scroll');

  } else {
    $('nav').removeClass('scroll');
    $('#no-active').removeClass('active');
 }
});



$(window).scroll(function() {
  if ($(document).scrollTop() > 200) {
    $('#about-heading').addClass('animated fadeIn');
    $('#key-features').addClass('animated fadeIn');
      $('.company-content').addClass('animated fadeIn');
  }
});

$(window).scroll(function() {
  if ($(document).scrollTop() > 1100) {
    $('.we_do').addClass('animated fadeIn');

  }
});

$(window).scroll(function() {
  if ($(document).scrollTop() > 1600) {
    $('#team-heading').addClass('animated fadeIn');
    $('#team-features').addClass('animated fadeIn');
      $('.team-content').addClass('animated fadeIn');
  }
});

$(window).scroll(function() {
  if ($(document).scrollTop() > 2200) {
    $('#feedback-heading').addClass('animated fadeIn');
    $('#feedback-features').addClass('animated fadeIn');
      $('.feedback-box').addClass('animated fadeIn');
  }
});


/*

// Set the date we're counting down to
var countDownDate = new Date("september 20, 2017 20:12:25").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    
    // Find the distance between now an the count down date
    var distance = countDownDate - now;
    
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = days + "d "+" "+ hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "Launching In Moments..";
    }
}, 1000);


*/

function minname(){
    var value=$("#usr").val();
     var pass2 = document.getElementById('usr');
    var message = document.getElementById('confirmMessage2');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    if(value.length>=3){

                pass2.style.backgroundColor=goodColor;
        message.innerHTML="Verified!";
         message.style.color = goodColor;
    }
    else if(value.length<3){
        pass2.style.backgroundColor=badColor;
        message.innerHTML="Enter Min. 3 Alphabets!";
         message.style.color = badColor;
    }
}
          
          function minpass(){
    var value=$("#pwd").val();
     var pass2 = document.getElementById('pwd');
    var message = document.getElementById('confirmMessage3');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    if(value.length>=6){

                pass2.style.backgroundColor=goodColor;
        message.innerHTML="Verified!";
         message.style.color = goodColor;
    }
    else if(value.length<3){
        pass2.style.backgroundColor=badColor;
        message.innerHTML="Enter Min. 6 Alphabets!";
         message.style.color = badColor;
    }
}
      	
function checkPass()
{
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('pwd');
    var pass2 = document.getElementById('pwd2');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match!"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
}  






     $(document).ready(function(){
        $.ajax({
            url:"https://blockchain.info/ticker",
            success:function(result){
                console.log(result);
                $('#usdlast').html(result.USD.symbol+result.USD.last);
                $('#inrlast').html(result.INR.symbol+result.INR.last);
                $('#last').html(result.INR.symbol+result.INR.last);
 
                $('#buying').html(result.INR.symbol+result.INR.buy);
                $('#selling').html(result.INR.symbol+result.INR.sell);

            }
            
        }); 
     }); 
          
          function sendmail(){
            alert("You Will shortly receive an email in 30 minutes. Check you inbox.");  
          }
      