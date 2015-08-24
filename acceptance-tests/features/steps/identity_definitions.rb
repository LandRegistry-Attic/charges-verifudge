Given(/^I am on the identity list$/) do
  visit "#{Urls.verifudge}/identity"
  assert page.has_content?('All Identities')
  @table_rows = page.all(:css, 'table tr').count
end

When(
  /^I create an identity for (\w+)((?: \w+)+)* (\w+):$/
) do |first_name, middle_names, last_name, table|
  visit "#{Urls.verifudge}/identity/new"
  fill_in('first_name', with: first_name)
  fill_in('middle_names', with: middle_names)
  fill_in('last_name', with: last_name)

  details = table.rows_hash

  dob = Date.parse(details['dob'])

  fill_in('dob_day', with: dob.day)
  fill_in('dob_month', with: dob.month)
  fill_in('dob_year', with: dob.year)

  fill_in('address_line1', with: details['address_line1'])
  fill_in('postcode', with: details['postcode'])
  select(details['gender'], from: 'gender')

  click_button 'Create new Identity'
end

Then(
  /^(\w+)( (?:\w+)+)* (\w+) should be listed on the identity list$/
) do |first_name, middle_names, last_name|
  full_name = [first_name, middle_names, last_name]
              .select { |str| str.to_s != '' }
              .join(' ')
  assert page.has_content?(full_name)
  @row = page.first(:css, 'table tr', text: full_name)
  @identity_id = @row.all(:css, 'td')[0].text
end

Then(
  /^(\w+)((?: \w+)+)* (\w+)'s date of birth is ([A-Za-z0-9 ]+)$/
) do |_first_name, _middle_names, _last_name, date|
  date = Date.parse(date)
  assert @row.has_content?("#{date.day}-#{date.month}-#{date.year}")
end

Then(
  /^(\w+)((?: \w+)+)* (\w+)'s address is ([A-Za-z0-9 ]+), ([A-Za-z0-9 ]+)$/
) do |_first_name, _middle_names, _last_name, address, postcode|
  assert @row.has_content?(address)
  assert @row.has_content?(postcode)
end

Then(
  /^(\w+)((?: \w+)+)* (\w+)'s gender is (\w+)$/
) do |_first_name, _middle_names, _last_name, gender|
  assert @row.has_content?(gender.upcase)
end
