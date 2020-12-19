import React from 'react'
import './App.css'
import Dashboard from './pages/dashboard'
import { Route, Switch, BrowserRouter } from 'react-router-dom'

function App() {
  return (
      <div>
        <BrowserRouter >
        <Switch>
            <Route exact path="/" component={Dashboard}/>
        </Switch>
        </BrowserRouter>
      </div>
  )
}
export default App