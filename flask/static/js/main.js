var teamResult = document.getElementById('team-result');
var projectResult = document.getElementById('project-result');

function getData() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      fillData(this.responseText)
    }
  };
  setTimeout(function() {
    getData();
  }, 10000);
  //[[{"name": "xxx", "votes": 123}],[{"name": "xxx", "votes": 123}]]
  xhttp.open("GET", "getData", true);
  xhttp.send();
}

function fillData(data) {
  data = JSON.parse(data)
  console.log(data);
  for (var i = 0; i < 10; i++) {
    teamResult.children[0].children[i + 1].children[0].innerHTML = data[0][i]["name"];
    teamResult.children[0].children[i + 1].children[1].innerHTML = data[0][i]["votes"];
    projectResult.children[0].children[i + 1].children[0].innerHTML = data[1][i]["name"];
    projectResult.children[0].children[i + 1].children[1].innerHTML = data[1][i]["votes"];
  }
}
function init() {
  for (var i = 0; i < 10; i++) {
    var tr = document.createElement('tr');
    tr.innerHTML = '<td class="team-name"></td><td class="team-votes"></td>';
    teamResult.children[0].appendChild(tr);
    var tr2 = document.createElement('tr');
    tr2.innerHTML = '<td class="project-name"></td><td class="project-votes"></td>';
    projectResult.children[0].appendChild(tr2);
  }
}

window.onload = function () {
  init();
  getData();
}

