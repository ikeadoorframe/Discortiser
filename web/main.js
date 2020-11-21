  function StartButton(){
    var server_invite = document.getElementById("server_invite").value;
    var post_delay = document.getElementById("post_delay").value;
    var delay_type = document.getElementById("delay_type").value;
    eel.main(server_invite, post_delay, delay_type);
  }

function OpenAds(){
  eel.OpenAds()
}

function OpenAccounts(){
  eel.OpenAccounts()
}

function sendLog(text){
var log = document.getElementById('ConsoleLog');
  log.value += text;
  log.scrollTop = log.scrollHeight;
}
eel.expose(sendLog);
