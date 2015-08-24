Given(/^I visit the Hello World page$/) do
  visit("#{Urls.verifudge}/helloworld")
end

Then(/^the page contains Hello World! \(assert_selector\)$/) do
  assert_selector("//*[@id='content']/h1", text: 'Hello, World!')
end

Then(/^the page contains Hello World! \(assert_match\)$/) do
  assert_match('Hello, World!', page.body, 'Error: Expected Hello, World!')
end

Then(/^the page does not contain Goodbye World!$/) do
  assert_no_selector("//*[@id='content']/h1", text: 'Goodbye, World!')
end
