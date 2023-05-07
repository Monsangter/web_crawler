import schedule as sch
import time
import threading


from crawler import WantedCrawler, JobKoreaCrawler, SaraminCrawler

def run_crawlers():
    wanted_url = 'https://www.wanted.co.kr/wdlist/518/899?country=kr&job_sort=company.response_rate_order&years=0&years=1&locations=seoul.all'
    jobkorea_url = 'https://www.jobkorea.co.kr/Search/?stext=python&local=I000&careerType=1&tabType=recruit'
    saramin_url = 'https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=python&loc_mcd=101000&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&exp_cd=1%2C2&exp_max=1&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPageCount=20&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n'

    wanted_crawler = WantedCrawler(wanted_url)
    jobkorea_crawler = JobKoreaCrawler(jobkorea_url)
    saramin_crawler = SaraminCrawler(saramin_url)

    threads = [
        threading.Thread(target=wanted_crawler.crawl),
        threading.Thread(target=jobkorea_crawler.crawl),
        threading.Thread(target=saramin_crawler.crawl)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def start_scheduler():
    try:
        run_crawlers() # 초기 한 번 실행

        sch.every().day.at("00:00").do(run_crawlers) # 매일 00시에 실행

        while True:
            sch.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"{e}")