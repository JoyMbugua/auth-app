import React, { Component } from "react";
import { Switch, Link, Route } from "react-router-dom";
import Signup from "./Signup";


class App extends Component{
   render(){
    return(
        <div className="site">
        <nav>
            <Link className={"nav-link"} to={"/"}>Home</Link>
            <Link className={"nav-link"} to={"/signup/"}>Signup</Link>
        </nav>
        <main>
           

            <Switch>
                <Route exact path={"/signup/"} component={Signup}/>
                <Route path={"/"} render={() => <div>Home again</div>}/>
            </Switch>
        </main>
    </div>
    );
  }
}

export default App;