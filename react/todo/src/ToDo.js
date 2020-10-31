import React, { Component } from 'react';

export default class Todo extends Component {
  constructor() {
    super();
    this.state = {
      todo_array: [],
      task: '',
      edit_task: ''
    };
  }

  onChangeTask = (e) => {
    this.setState({
      task: e.target.value
    });
  }

  addTask = () => {
    let { todo_array, task } = this.state;
    let obj = {
      id: todo_array.length == 0 ? 1 : todo_array[todo_array.length - 1].id + 1,
      name: task,
      is_editing: false,
      is_done: false
    };
    todo_array.push(obj);
    this.setState({
      todo_array: todo_array,
      task: ''
    });
  }

  edit = (object) => {
    console.log('edit', object);
    let { todo_array } = this.state;

    let i = todo_array.findIndex(task => task.id === object.id);
    todo_array[i].is_editing = !todo_array[i].is_editing;

    todo_array.map((task) => { task.id !== object.id ? task.is_editing = false : task.is_editing = task.is_editing; return task });

    this.setState({
      todo_array: todo_array,
      edit_task: object.name
    }, () => {
      console.log(this.state.todo_array)
    });

  };

  editTask = (task) => {
    this.setState({
      edit_task: task
    });
  }

  saveEditTask = (object) => {
    console.log('saveEditTask', object);
    let { todo_array, edit_task } = this.state;
    let i = todo_array.findIndex(task => task.id === object.id);
    todo_array[i].name = edit_task;

    this.setState({
      todo_array: todo_array,
      edit_task: ''
    }, (e) => {
      this.edit(object);
    });
  }

  delete = (object) => {
    // console.log('delete', object);
    let { todo_array } = this.state;
    let i = todo_array.findIndex(task => task.id === object.id);
    todo_array.splice(i, 1);
    this.setState({
      todo_array: todo_array
    }, (e) => {
    });
  }

  done = (object) => {
    let { todo_array } = this.state;
    let i = todo_array.findIndex(task => task.id === object.id);
    todo_array[i].is_done = true;

    this.setState({
      todo_array: todo_array
    }, (e) => {
      console.log('done', this.state.todo_array);
    });
  }

  render() {
    return (

      <div className="ui container comments">

        <div className="form-group">
          <input
            type="text"
            className="form-control"
            value={this.state.task}
            onChange={this.onChangeTask}
            placeholder='Add your task'
          />
          <button disabled={this.state.task == ''} onClick={this.addTask}>
            Add Task
          </button>
        </div>

        <div>
          {this.state.todo_array.length > 0 ? (<table style={{ marginTop: 20 }}>
            <thead>
              <tr>
                <th>Task</th>
                <th>Action</th>
              </tr>
            </thead>
            {
              this.state.todo_array.map((object, i) => {
                return (
                  <tbody>
                    <tr>
                      <td>
                        {object.is_editing ? <input value={this.state.edit_task} onChange={e => this.editTask(e.target.value)} /> :
                          object.is_done ? <s>{object.name}</s> : <span>{object.name}</span>}
                      </td>
                      <td>
                        {object.is_editing ?
                          <div>
                            <button onClick={e => this.saveEditTask(object)} className="btn btn-danger">Save</button>
                            <button onClick={e => this.edit(object)} className="btn btn-danger">Cancel</button>
                          </div>
                          :
                          <div>
                            <button onClick={e => this.edit(object)} className="btn btn-danger">Edit</button>
                            <button onClick={e => this.done(object)} className="btn btn-danger">Done</button>
                            <button onClick={e => this.delete(object)} className="btn btn-danger">Delete</button>
                          </div>}

                      </td>
                    </tr>
                  </tbody>
                )
              })}
          </table>) : ('No task to do!')}
        </div>

      </div>
    );
  }
};