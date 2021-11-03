import './App.css';
import React ,{useState}from 'react'
import { CURLParser } from 'parse-curl-js'
import parse from 'parse-curl'
import axios from 'axios';

function generateSuccessHTMLOutput(response) {
  return  '<h4>Result</h4>' + 
          '<h5>Data from API:</h5>' + 
          '<pre>' + JSON.stringify(response.data, null, '\t') + '</pre>'; 
}

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      query: null,
      data:null,
    };
    
    this.publish = this.publish.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  
  handleChange({ target }) {
    this.setState({
      [target.name]: target.value
    });
  }

  publish() {
    var resultElement = document.getElementById('postResult');
    resultElement.innerHTML = '';
    console.log( this.state.query);
    const cURLParser2 = new CURLParser(this.state.query)
    // cURLParser.parse().body.data
    const cURLParser = parse(this.state.query)
    console.log('json', cURLParser)
    const requestOptions = {
      method: cURLParser.method,
      headers:  CURLParser.headers,
      };

    if(requestOptions.method=='GET'|| requestOptions.method=='DELETE'){
      axios({method:requestOptions.method,
        url: cURLParser.url,
        headers: requestOptions.headers,
      })
      .then((data) => {resultElement.innerHTML = generateSuccessHTMLOutput(data)} )
      .catch((error) => console.log(error))
    }
    
    else{
      console.log(JSON.stringify(cURLParser2.parse().body.data))
      axios({method:requestOptions.method,
        url: cURLParser.url,
        data: cURLParser2.parse().body.data,
        headers: requestOptions.headers,
      })
      .then((data) => {resultElement.innerHTML = generateSuccessHTMLOutput(data)})
      .catch((error) => console.log(error))
    }
  };
  
  render() {
    return <div>
      <input 
        style={{ width:500, borderWidth: 2 }}
        type="text" 
        name="query" 
        placeholder="Enter curl query here..." 
        value={ this.state.query }
        onChange={ this.handleChange} 
      />
      <button value="Send" onClick={this.publish}>Run Query</button>
      
    </div>
  }
}

export default App;