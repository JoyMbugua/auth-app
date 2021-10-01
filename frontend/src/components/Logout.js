import React, {Component} from "react";

class Logout extends Component{
    constructor(){
        super()
        this.handleLogout = this.handleLogout.bind(this)
    }

    handleLogout(e){
        e.preventDefault();
        localStorage.clear();
        window.location.replace('/login/')
    }
    render(){
       return(
        <main>
            <div className="logoutinputs">
            <p className="centered-text">Are you sure you want to logout?</p>
             <input type="submit" value="Logout" onClick={this.handleLogout} />
            </div>
    </main>
       )
    }
}
export default Logout;