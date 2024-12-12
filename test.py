'''def lambda_handler(event, context):
    driver = None
    try:
        driver = setup_driver()
        
        # StockBubble screenshot
        driver.get('https://stockbubble.in/')
        time.sleep(2)
        screenshot_file = take_screenshot(driver)
        
        # Get advances/declines
        driver.get('https://www.nseindia.com/')
        time.sleep(2)
        num_adv, num_dec = get_advance_decline_values_xpath(driver)
        
        # Get FII/DII data
        driver.get('https://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/index.php')
        time.sleep(2)
        net_fii, net_dii = get_fii_dii_values_xpath(driver)
        
        # Post to Twitter
        try:
            driver.get('https://x.com/i/flow/login')
            load_cookies(driver, '/opt/x.json')  # Adjust path as needed
            driver.refresh()
            driver.get('https://x.com/compose/post')
            
            tweet_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]'))
            )
            
            fii_message, dii_message = format_fii_dii_message(net_fii, net_dii)
            message = (
                f"Advances : {num_adv} & Declines : {num_dec} in Nifty50\n\n"
                f"{fii_message} cr and {dii_message} cr"
            )
            tweet_box.send_keys(message)
            
            # Upload screenshot
            media_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="fileInput"]')
            media_button.send_keys(screenshot_file)
            
            time.sleep(3)
            post_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
            post_button.click()
            time.sleep(5)
            
            return {
                'statusCode': 200,
                'body': json.dumps('Tweet posted successfully')
            }
            
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error posting tweet: {str(e)}')
            }
            
    except Exception as e:
        print(f"General error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
        
    finally:
        if driver:
            driver.quit()'''