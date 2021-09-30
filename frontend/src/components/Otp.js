import React, { Component } from "react";
import CSRFToken from "./Csrf";

class OTPView extends Component{
    constructor(props) {
        super(props);
        this.state = {
            otpCode: ""
        }
       
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(event){
        this.setState({otpCode: event.target.value})
    }

    async handleSubmit(event){
        console.log("state",this.state)
        event.preventDefault();
        try{
            
            await axios.post('http://127.0.0.1:8000/api/v1/verify/', {
                otpCode: this.state.otpCode
            })
            .then(resp => resp)
            .then(data => {
                console.log(data)
            })
        }catch(error){
            console.log(error)
        }
    }
 
    render() {
         return (
           <div>
             <form className="otpform" onSubmit={this.handleSubmit}>
               <CSRFToken />
               <label>
                  Enter OTP Code:{' '}
                 <input
                   name="username"
                   type="text"
                   onChange={this.handleChange}
                 />
               </label>
               <input type="submit" value="Send" />
             </form>
           </div>
         );
    }
}

export default OTPView;