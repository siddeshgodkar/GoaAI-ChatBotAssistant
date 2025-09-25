import {render, screen} from "@testing-library/react";
import '@testing-library/jest-dom';
import App from "../App";
import ChatBox from "../components/chatBox";

beforeAll(() => {
  // mock scrollIntoView so jsdom doesn't crash
  window.HTMLElement.prototype.scrollIntoView = function () {};
});


test("renders input box", () => {
  render(<ChatBox />);
  expect(screen.getByPlaceholderText("Ask me anything...")).toBeInTheDocument();
});