const onSerch = () => {
  let username = document.getElementById("serchNameInput").value;
  fetch(`http://127.0.0.1:3000/api/members?username=${username}`, {
    method: "get",
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => response.json())
    .then((obj) => {
      if (obj.data != null) {
        let memberName = obj.data.name;
        let memberUsername = obj.data.username;
        document.getElementById(
          "serchNameResult"
        ).textContent = `${memberName}(${memberUsername})`;
      }
    })
    .catch((error) => console.error("Error:", error));
};

const updateName = () => {
  if (document.getElementById("updateNameInput").value == "") {
    document.getElementById("updateNameResult").textContent = "請輸入新姓名";
  } else {
    let newName = document.getElementById("updateNameInput").value;
    fetch("http://127.0.0.1:3000/api/member", {
      method: "post",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: newName,
      }),
    })
      .then((response) => response.json())
      .then((res) => {
        if (res.error) {
          document.getElementById("updateNameResult").textContent = "更新失敗";
        }
        if (res.ok) {
          document.getElementById("updateNameResult").textContent = "更新成功";
          document.getElementById("currentName").textContent = newName;
        }
      })
      .catch((error) => console.error("Error:", error));
  }
};
