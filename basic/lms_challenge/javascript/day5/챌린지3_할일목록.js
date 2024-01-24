const todoList = document.getElementById('todo-list');
const todoForm = document.getElementById('todo-form');
let todos = [];


// storage
function saveTodos(){
  localStorage.setItem('myTodos', JSON.stringify(todos));
}

function getTodos(){
  const storagedTodos = localStorage.getItem('myTodos');
  if(storagedTodos === null) return;
  todos = JSON.parse(storagedTodos);
  displayTodos();
}
getTodos();

// create update delete read
// read
function displayTodos() {
  todoList.innerHTML = '';
  todos.forEach((todo) => {
    const todoItem = document.createElement('li');
    todoItem.title = '클릭하면 완료';
    todoItem.innerText = todo.todoText;
    todoItem.addEventListener('click', () => {
      doneTodo(todo.todoId);
    });
    if(todo.todoDone){
      todoItem.classList.add('done');
    }else {
      todoItem.classList.remove('done');
    }

    const deleteBtn = document.createElement('span');
    deleteBtn.title = '클릭하면 삭제';
    deleteBtn.innerText = 'x';
    deleteBtn.addEventListener('click', () => {
      deleteTodo(todo.todoId);
    });
    todoItem.appendChild(deleteBtn);

    todoList.appendChild(todoItem);
  });
};

// delete
function deleteTodo(clickedId) {
  todos = todos.filter((todo) => todo.todoId !== clickedId);
  displayTodos();
  saveTodos();
};

// update(done)
function doneTodo(clickedId) {
  todos.forEach(todo => {
    if(todo.todoId === clickedId){
      todo.todoDone = !todo.todoDone;
    }
  })
  displayTodos();
  saveTodos();
}

// create
todoForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const trimValue = todoForm.todo.value.trim();
  if (trimValue === '') return;
  const toBeAdded = {
    todoText: trimValue,
    todoId: new Date().getTime() + '',
    todoDone: false,
  };
  todos.push(toBeAdded);
  todoForm.todo.value = '';
  todoForm.todo.focus();
  displayTodos();
  saveTodos();
});
