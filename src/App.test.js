import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";

test("Login Button", () => {
  const result = render(<App />);
  const LoginBtnElement = screen.getByText("Submit");
  expect(LoginBtnElement).toBeInTheDocument();

  fireEvent.click(LoginBtnElement);
  const ReplayBtnElement = screen.getByText("Play Again!");
  expect(ReplayBtnElement).toBeInTheDocument();
});

test("Play Again Button", () => {
  const result = render(<App />);
  const LoginBtnElement = screen.getByText("Submit");
  expect(LoginBtnElement).toBeInTheDocument();

  fireEvent.click(LoginBtnElement);
  const ReplayBtnElement = screen.getByText("Play Again!");
  expect(ReplayBtnElement).toBeInTheDocument();

  fireEvent.click(ReplayBtnElement);
  expect(ReplayBtnElement).toBeInTheDocument();
});

test("Show/Hide LeaderBoard", () => {
  const result = render(<App />);
  const LoginBtnElement = screen.getByText("Submit");
  expect(LoginBtnElement).toBeInTheDocument();

  fireEvent.click(LoginBtnElement);
  const LeaderBoardBtnElement = screen.getByText("Leader Board");
  expect(LeaderBoardBtnElement).toBeInTheDocument();

  fireEvent.click(LeaderBoardBtnElement);
  const UserList_Element = screen.getByText("UserName");
  expect(UserList_Element).toBeInTheDocument();
});

test("Playing And Watching", () => {
  const result = render(<App />);
  const LoginBtnElement = screen.getByText("Submit");
  expect(LoginBtnElement).toBeInTheDocument();

  fireEvent.click(LoginBtnElement);
  const Playing_Element = screen.getByText("Currently Playing:");
  const Watching_Element = screen.getByText("Currently Watching:");
  expect(Playing_Element).toBeInTheDocument();
  expect(Watching_Element).toBeInTheDocument();
});
