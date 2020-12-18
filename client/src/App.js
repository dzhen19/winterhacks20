import React from 'react'
import './App.css'
import Map from  './components/map'
import { Route, Switch, BrowserRouter } from 'react-router-dom'

function App() {
  return (
      <div>
        <BrowserRouter >
        <Switch>
            <Route exact path="/" component={Map} />
        </Switch>
        </BrowserRouter>
      </div>
  )
}
export default App