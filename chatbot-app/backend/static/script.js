// async function sendMessage() {
//     const message = document.getElementById("message").value;
//     const res = await fetch("/chat", {
//         method: "POST",
//         headers: {"Content-Type": "application/json"},
//         body: JSON.stringify({message})
//     });
//     const data = await res.json();
//     document.getElementById("chatReply").innerText = data.reply;
// }


async function sendMessage() {
            let msg = document.getElementById("message").value;
            if (!msg) return;

            document.getElementById("chatbox").innerHTML += `<p class="user"><b>You:</b> ${msg}</p>`;
            document.getElementById("message").value = "";

            fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: msg })
            })
                .then(res => res.json())
                .then(data => {
                    document.getElementById("chatbox").innerHTML += `<p class="bot"><b>Bot:</b> ${data.reply}</p>`;
                    document.getElementById("chatbox").scrollTop = document.getElementById("chatbox").scrollHeight;
                });
        }


// async function searchMap() {
//     const location = document.getElementById("location").value;
//     const res = await fetch(`/map-search?query=${location}`);
//     const data = await res.json();
//     document.getElementById("mapResults").innerText = JSON.stringify(data, null, 2);
// }
