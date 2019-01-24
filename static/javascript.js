function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
    return false;
  }
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }



  // Sign up
  var log = '{{log}}';
  if (log=='false') {
    var str1 = "Sign Up";
    var result1 = str1.link("{{url_for('SignUp')}}");
    document.getElementById("signup").classList.add("nav-link");
    document.getElementById("signup").innerHTML = result1;
  }



  // Log in
  var str;
  var result;
  document.getElementById("demo").classList.add("nav-link");
  if ({{log}}=='true') {
    str = "Log Out";
    result = str.link("{{url_for('Login')}}");
  }
  else{
    str = "Log in";
    result = str.link("{{url_for('Login')}}");
  }

  console.log(result)
  document.getElementById("demo").innerHTML = result;