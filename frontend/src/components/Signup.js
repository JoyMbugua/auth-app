import React, { Component } from 'react';
import axios from 'axios';
import CSRFToken from './Csrf';


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class Signup extends Component{
  constructor(props){
    super(props);

    this.state = {
        username: "",
        email: "", 
      
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
      this.setState({ [event.target.name]: event.target.value });
    //   console.log(this.state[event.target.name])
  }

  async handleSubmit(event){
    event.preventDefault();
    try{
        const user = {
            username: this.state.username,
            email: this.state.email,
          };
        //   alert('usercreated!' + this.state.username)
        //   window.location.replace('http://127.0.0.1:8000/')
          
         await axios.post('http://127.0.0.1:8000/api/v1/users/register/', {
            
             username: this.state.username,
             email: this.state.email,
            
         })
          .then(res => res)
          .then(result => {
              
              if(result.status === 201){
                  window.location.replace('http://127.0.0.1:8000/')
              }
          }) 
    }catch(error){
      console.log(error.stack)
      this.setState({
        errors:error.response.data
      })
    }
  }

  render(){
    return(
      <div>
          <h2>Signup Page</h2>
            <form onSubmit={ this.handleSubmit }>
            <CSRFToken />
            <label>
                Username:
                <input name="username" type="text" value={this.state.username} onChange={this.handleChange} />
               
            </label>
            <label>
                Email:
                <input name="email" type="email" value={this.state.email} onChange={this.handleChange} />
                
            </label>

            <input type="submit" value="Submit" />
          </form>
      </div>
    )
  }
}

export default Signup;


