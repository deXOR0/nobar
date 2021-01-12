document.getElementById("submitButton").onclick = function () {
  const movie = document.getElementById("movie").value;
  const title = movie.substring(movie.lastIndexOf("\\") + 1);
  const subtitle = document.getElementById("subtitle").value;
  console.log(title);
  console.log(movie);
  console.log(subtitle);
  const str =
    '<video width="1280" height="720" controls autoplay> <source src="' +
    movie +
    '" type="video/mp4"/>' +
    '"<track default src="' +
    subtitle +
    '" kind="captions" srclang="en" label="English"/> </video>';
  document.getElementById("video").innerHTML = str;
  document.getElementById("title").innerHTML = title;
};

document.getElementById("browseMovieButton").onclick = function () {
  // alert("aaa");
  jQuery.getJSON(
    "http://127.0.0.1:5000/get_movie",
    function (data, textStatus, jqXHR) {
      document.getElementById("movie").value = data;
    }
  );
};

document.getElementById("browseSubtitleButton").onclick = function () {
  // alert("aaa");
  jQuery.getJSON(
    "http://127.0.0.1:5000/get_subtitle",
    function (data, textStatus, jqXHR) {
      document.getElementById("subtitle").value = data;
    }
  );
};
