var tablinks =document.getElementsByClassName("tab-link");
var tabcontents =document.getElementsByClassName("tab-content");

function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove("active-link");
    }

    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}

document.getElementById("myLoc").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default anchor click behavior
    // Change iframe src to load a specific section
    document.getElementById("mapSection").scrollIntoView({ behavior: 'smooth' });
});