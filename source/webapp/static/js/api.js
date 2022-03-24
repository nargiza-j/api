let buttons = document.getElementsByName('button');
let answerField = document.getElementById('answer-field');
let answer = document.getElementById('answer');

async function request(event, method='POST') {
    let eventTarget = event.target;
    let url = eventTarget.dataset.href;
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let data = {
        'A': document.getElementById('first').value,
        'B': document.getElementById('second').value
    }
    let response = await fetch(url, {
        'method': 'POST',
        'body': JSON.stringify(data),
        'headers': {
            'X-CSRFToken': csrftoken
        }
    });
    let responseBody = await response.json();
    if (response.ok) {
        answerField.style.backgroundColor = 'green';
        answer.innerText = responseBody['answer'];
    } else {
        answerField.style.backgroundColor = 'red';
        answer.innerText = responseBody['error'];
    }
}

window.addEventListener('load', function() {
    for (let i=0; i<buttons.length; i++) {
            buttons[i].addEventListener('click', request)
    }
})