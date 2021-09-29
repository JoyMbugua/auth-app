import React, { Component } from "react";
import CSRFToken from "./Csrf";

class OTPView extends Component{
 
    render() {
         return (
           <div>
             <form className="otpform">
               <CSRFToken />
               <label>
                         Enter OTP Code:{' '}
                 <input
                   name="username"
                   type="text"
                 />
               </label>
               <input type="submit" value="Send" />
             </form>
           </div>
         );
    }
}

export default OTPView;