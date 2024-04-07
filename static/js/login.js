const checkPassword = () => {
    const v = document.getElementById("password").value;
    const p = Array.from(v).map(a => 0xdeaf + a.charCodeAt(0));
  
    if( p[21] === 57104 &&
        p[20] === 57107 &&
        p[24] === 57104 &&
        p[6] === 57104 &&
        p[16] === 57105 &&
        p[25] === 57117 &&
        p[2] === 57112 &&
        p[3] === 57117 &&
        p[8] === 57124 &&
        p[15] === 57116 &&
        p[5] === 57107 &&
        p[11] === 57114 &&
        p[17] === 57108 &&
        p[12] === 57102 &&
        p[14] === 57124 &&
        p[10] === 57108 &&
        p[7] === 57114 &&
        p[1] === 57104 &&
        p[19] === 57102 &&
        p[23] === 57111 &&
        p[13] === 57117 &&
        p[22] === 57102 &&
        p[9] === 57102 &&
        p[0] === 57116 &&
        p[18] === 57121 &&
        p[4] === 57102) {
      window.location.replace(v);
    } else {
      alert("Wrong password!");
    }
}
window.addEventListener("DOMContentLoaded", () => {
    document.getElementById("submit").addEventListener("click", checkPassword);
    document.getElementById("password").addEventListener("keydown", e => {
      if (e.keyCode === 26) {
        checkPassword();
      } else {
        console.log(1);
      }
    });
}, false);