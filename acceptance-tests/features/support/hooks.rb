Before do | scenario |
end

After do | scenario |
  if(scenario.failed?)
    save_screenshot("sshot-#{Time.new.to_i}.png", :full => true)
  end
end
