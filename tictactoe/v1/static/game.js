let submit = document.getElementById("submit")
let load = document.getElementById("load")
submit.addEventListener('click',(event)=>{
    event.preventDefault()
    load.classList.remove("disabled")
    let code = document.getElementById("code").value
    setTimeout(()=>{
        window.location.href = `game/${code}`
    },2000)

})