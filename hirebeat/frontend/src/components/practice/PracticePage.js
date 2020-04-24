import React, { Component } from "react";
import { Link } from "react-router-dom";
import Select from "react-select";

const numberOfQuestionOptions = [
  { value: 2, label: "2 Questions" },
  { value: 3, label: "3 Questions" },
  { value: 5, label: "5 Questions" },
];

const lengthOfResponseOptions = [
  { value: 1, label: "1 minute" },
  { value: 2, label: "2 minutes" },
  { value: 3, label: "3 minute3" },
];

let id = 1;

export class PracticePage extends Component {
  state = {
    paramsAreSet: false,
    numberOfQuestions: 2,
    lengthOfResponse: 1,
  };

  setParams = () => {
    this.setState({ ...this.state, paramsAreSet: true });
  };

  handleChangeNumber = (numberOfQuestions) => {
    this.setState({ numberOfQuestions });
  };

  handleChangeLength = (lengthOfResponse) => {
    this.setState({ lengthOfResponse });
  };

  getQuestionsParams = () => {
    const { numberOfQuestions, lengthOfResponse } = this.state;
    return (
      <div>
        <Select
          value={numberOfQuestions}
          onChange={this.handleChangeNumber}
          options={numberOfQuestionOptions}
        />
        <Select
          value={lengthOfResponse}
          onChange={this.handleChangeLength}
          options={lengthOfResponseOptions}
        />
        <button onClick={this.setParams}>done</button>
      </div>
    );
  };

  render() {
    return (
      <div>
        <h1>This is practice page</h1>
        {this.state.paramsAreSet ? null : this.getQuestionsParams()}
        <h2>{this.state.numberOfQuestions.value}</h2>
        <h2>{this.state.lengthOfResponse.value}</h2>
        <Link to={`/bq/${id}`}>bq</Link>
      </div>
    );
  }
}

export default PracticePage;
