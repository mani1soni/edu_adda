// import react and reactDOM library
import React from 'react';
import ReactDOM from 'react-dom';
import ToDo from './ToDo'

const App = () => {
    return (
        <ToDo />
    )
};

ReactDOM.render(
    <App />,
    document.querySelector('#root')
)