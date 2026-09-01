from client import InfluencerAffiliateAttributionConversionAggregatorClient

def main():
    client = InfluencerAffiliateAttributionConversionAggregatorClient()
    res = client.aggregate_affiliate_conversions('ALEX15', 30)
    print('Affiliate Attribution Aggregator: ' + res['attribution_batch_id'] + ' (Code: ' + res['promo_code'] + ')')
    print('Orders: ' + str(res['total_attributed_orders_count']) + ' | GMV: $' + str(res['gross_merchandise_value_usd']))
    print('Commission: $' + str(res['creator_commission_earned_usd']) + ' | ROAS: ' + str(res['return_on_ad_spend_roas']) + 'x')
    print('Payout CSV: ' + res['commission_payout_export_csv_url'])

if __name__ == '__main__':
    main()
