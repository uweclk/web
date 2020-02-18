import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            similar_words: [],
        };
    }

    componentDidMount() {
        axios.get('/api/v1/similar_words?term=water')
            .then((res) => {
                this.setState({
                    similar_words: res.data,
                });
            })
            .catch((err) => {
                console.error(err);
            });
    }

    render() {
        const { similar_words } = this.state;

        return (
            <div className="App">
                <ul>
                    {similar_words.map(word => (
                        <li key={word}>{word}</li>
                    ))}
                </ul>
            </div>
        );
    }
}

export default App;
