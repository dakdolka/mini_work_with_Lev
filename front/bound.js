function uppopup() {
    document.querySelector('.main_pu').classList.toggle('close') //document - корень, querySelector - выбор элемента хоть по айди, хоть по имени класса
    // toggle - если есть - удалит, если нет - добавит, для гениев
}

function take_info() {
    const input_elem = document.getElementById('News');
    alert(input_elem.value);
}

document.getElementById('main_form').addEventListener('submit', take_info);

async function get_content(){
    console.log('345678')
    const res = await fetch('http://127.0.0.1:8000/get_all')
    const data = await res.json()
    console.log(data)
    document.getElementById('popup-content').innerHTML = Object.values(data)
}

async function caller() {
    uppopup()
    await get_content()
}
