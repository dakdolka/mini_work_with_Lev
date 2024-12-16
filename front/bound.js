function uppopup() {
    document.querySelector('.main_pu').classList.toggle('close') //document - корень, querySelector - выбор элемента хоть по айди, хоть по имени класса
    // toggle - если есть - удалит, если нет - добавит, для гениев
}

function take_info() {
    const input_elem = document.getElementById('News');
    return input_elem.value
}

async function get_content(){
    const dannye = take_info()
    const res = await fetch('https://127.0.0.1:8000/add/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'info': dannye})
            //?info=dannye
        }
    )
    //добавили данные в таблицу - POST запрос, ничего не возвращает, а просто добавляет в таблицу данные

    const res2 = await fetch('https://127.0.0.1:8000/get_all/')
    const data = await res2.json()
    //получили все данные

    document.getElementById('popup-content').innerHTML = Object.values(data)
}

async function caller() {
    uppopup()
    await get_content()
}
