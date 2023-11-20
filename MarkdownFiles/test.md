# 概要

AWSおよびAzureから使用料金に関するデータを取得、計算し、作成したファイルをShare Pointに送信するプログラムです。

<img width="1161" alt="スクリーンショット 2023-11-07 9.51.12.png (386.9 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/11/07/155118/31300020-108d-40c3-a32c-9e9f4d542f25.png">
<img width="1161" alt="スクリーンショット 2023-11-07 9.51.44.png (340.6 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/11/07/155118/ff4dbeb3-8674-4452-8fdf-7146acf3a009.png">
<img width="1486" alt="スクリーンショット 2023-11-06 10.36.57.png (250.4 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/11/06/155118/acf20cc1-a01f-4c93-aede-00360e67312f.png">

# 運用方法
## 1.Azure 
### 1-1.テナント
「**毎月8日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[Azure: Azureテナントファイルの作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「MSPC/課金/請求履歴  」に移動してください。
2. 「定期購入および 1 回限りの購入 JPY」タブを開いてください。
3. 2種類の当月分の「調整 Gxxxxxxxxx 終了済みのダウンロード」csvファイルをダウンロードしてください。
4. ダウンロードした2種類のファイルを「TeamKuramane/.../07_202108以降の事務処理/YYYYMM/Azure」にアップロードしてください。
5. 「[Azureテナントファイル作成開始](https://auto-resale-system-fa.azurewebsites.net/api/azuretenantfilestosharepoint)  」を押下してください。
* 押下後、デフォルトのブラウザが開きます。
6. 約3分後、ブラウザ上で「Executed/Success in: HTTP triggered function:Azure TenantFilesToSharePoint」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
7. 「TeamKuramane/.../07_202108以降の事務処理/YYYYMM/Azure/Tenants」を確認してください。
8. 作成完了です。

### 1-2.サブスクリプション
「**毎月8日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[Azure: Azureサブスクリプションファイルの作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「MSPC/課金/請求履歴  」に移動してください。
2. 「定期購入および 1 回限りの購入 JPY」タブを開いてください。
3. 2種類の当月分の「毎日評価される使用量の調整 Gxxxxxxxxx 終了済みのダウンロード」をダウンロードしてください。
4. ダウンロードした2種類のファイルを「TeamKuramane/.../07_202108以降の事務処理/YYYYMM/Azure」にアップロードしてください。
5. 「[Azureサブスクリプションファイル作成開始 ](https://auto-resale-system-fa.azurewebsites.net/api/azuresubscriptionfilestosharepoint)」を押下してください。
> **注意**：現在不具合（おそらく原因はFunctions appのメモリ不足）があり、作成不可能です。作成時はローカルから行います。

* 押下後、デフォルトのブラウザが開きます。
6. 約5分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AzureSubscriptionFilesToSharePoint」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
7. 「TeamKuramane/.../07_202108以降の事務処理/YYYYMM/Azure/Subscriptions」を確認してください。
8. 作成完了です。

### 1-3.テナントとサブスクリプションの概要
「**毎月8日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[Azure: Azureサマリーファイルの作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
0. 前提として、Azureテナントファイル及びサブスクリプションファイルの作成を完了してください。
詳細は、
Azureテナントファイル：「表題: Azure: Azureテナントファイルの作成に関するお知らせ」をご確認ください。
Azureサブスクリプションファイル：「表題: Azure: Azureサブスクリプションファイルの作成に関するお知らせ」をご確認ください。
1. 「[Azureサマリーファイル作成開始](https://auto-resale-system-fa.azurewebsites.net/api/azuresummaryfortenantsandsubscriptions) 」を押下してください。
* 押下後、デフォルトのブラウザが開きます。
2. 約1分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AzureSummaryForTenantsAndSubscriptions」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
3. TeamKuramane/.../07_202108以降の事務処理/YYYYMM/Azureを確認してください。
4. 作成完了です。

## 2.AWS
### 2-1.テナント
「**毎月4日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[AWS: 請求書PDFファイル作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「[請求書PDF作成開始](https://auto-resale-system-fa.azurewebsites.net/api/awss3tosharepoint)」を押下
* 押下後、デフォルトのブラウザが開きます。
2. 約1分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AWSS3ToSharePoint」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
3. TeamKuramane/.../07_202108以降の事務処理/YYYYMM/YYYYMM月度AWS を確認してください。
4. 作成完了です。

### 2-2.今月分の仮計上ファイルの作成
「**毎月26日の9時**」に受け取る通知の指示に従ってください。(26日に設定した理由: 今月分の仮計上記録は原則最終営業日に行うが、休日などを考慮した結果、本作業は少なくとも26日以降に行うため)
通知のタイトル: 「[AWS: 今月分の仮計上ファイル作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「AWS/Billing/請求書」に移動してください。
2. 請求期間が当月分であることを確認し、「すべてをcsvにダウンロード」を押下してください。
3. 「TeamKuramane/.../07_202108以降の事務処理/YYYYMM月度AWS計上資料」にcsvファイルをアップロードしてください。
4. csvファイルをxlsxファイルとして編集し、アップロードしてください。編集内容は以下の通りです。
- ファイル名 : ecsv_M_YYYY_仮計上_月中.xlsx
（例：ecsv_9_2023_仮計上_月中.xlsx）
- AD列1行目 : 「ExchangeRate」
- AD列2行目~AD列最終行 : 三菱UFJ銀行為替レート にて取得した「US Dollar: 月中平均TTS Monthly-Average TTS」を入力
* 対象セルを全選択し、値入力後、「ctr + Enter」で自動入力可能です。
> 為替レートを追加する際は、以下の画像を参照してください
> <img width="387" alt="スクリーンショット 2023-10-19 16.12.20.png (97.5 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/10/19/155118/5fcb6b0e-7159-4749-8fa1-757618789940.png">
5. 「[今月分の仮計上ファイル作成開始 ](https://auto-resale-system-fa.azurewebsites.net/api/awsrecordsforinvoices0monthago)」を押下してください。
* 押下後、デフォルトのブラウザが開きます。
6. 約1分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AWSRecordsForInvoices0MonthAgo」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
7. 「TeamKuramane/.../07_202108以降の事務処理/YYYMM/YYYYMM月度AWS計上資料」 を確認してください。
8. 作成完了です。

> **警告**
> 新しいテナントを追加または既存のテナントを削除する際、以下の文書を修正する必要があります。[①SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_アカウント管理](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BAA322803-25D6-4119-9139-E1D50F7AEE5D%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E7%AE¡A7%BD%E7%90%86.xlsx&action=default&mobileredirect=true), 
[②SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_計上資料_基礎情報.xlsx](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BEFDFCF03-128F-4913-9065-B87B3CDFAB68%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E8%A8¡A4%B8%8A%E8%B3%87%E6%96%99_%E5%9FºA4%8E%E6%83%85%E5%A0%B3.xlsx&action=default&mobileredirect=true)
理由は、ファンクションアプリがファイルを参照しているためです。
組織を削除する際、特定の列自体を削除する必要があります。中身だけを削除するのではありません。
組織を追加する際、リストの最後に情報を追加する必要があります。

### 2-3.先月分の仮計上ファイルの作成
「**毎月1日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[AWS: 先月分の仮計上ファイル作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「AWS/Billing/請求書」に移動してください。
2. 請求期間が先月分であることを確認し、「すべてをcsvにダウンロード」を押下してください。
3. 「TeamKuramane/.../07_202108以降の事務処理/YYYYMM月度AWS計上資料」にcsvファイルをアップロードしてください。
4. csvファイルをxlsxファイルとして編集し、アップロードしてください。編集内容は以下の通りです。
- ファイル名 : ecsv_M_YYYY_仮計上_月後.xlsx
（例：ecsv_9_2023_仮計上_月中.xlsx）
- AD列1行目 : 「ExchangeRate」
- AD列2行目~AD列最終行 : 「AWS/Billing/請求書」で確認した為替レートを入力
* 対象セルを全選択し、値入力後、「ctr + Enter」で自動入力可能です。
> 為替レートを追加する際は、以下の画像を参照してください
> <img width="387" alt="スクリーンショット 2023-10-19 16.12.20.png (97.5 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/10/19/155118/5fcb6b0e-7159-4749-8fa1-757618789940.png">
5. 「[先月分の仮計上ファイル作成開始](https://auto-resale-system-fa.azurewebsites.net/api/awsrecordsforinvoices1monthago)  」を押下してください。
* 押下後、デフォルトのブラウザが開きます。
6. 約1分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AWSRecordsForInvoices1MonthAgo」の表示を確認してください。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
* 不明点がある場合ドキュメント を参照してください。
7. 「TeamKuramane/.../07_202108以降の事務処理/YYYMM/YYYYMM月度AWS計上資料」 を確認してください。
8. 作成完了です。


> **警告**
> 新しいテナントを追加または既存のテナントを削除する際、以下の文書を修正する必要があります。[①SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_アカウント管理](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BAA322803-25D6-4119-9139-E1D50F7AEE5D%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E7%AE¡A7%BD%E7%90%86.xlsx&action=default&mobileredirect=true), 
[②SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_計上資料_基礎情報.xlsx](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BEFDFCF03-128F-4913-9065-B87B3CDFAB68%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E8%A8¡A4%B8%8A%E8%B3%87%E6%96%99_%E5%9FºA4%8E%E6%83%85%E5%A0%B3.xlsx&action=default&mobileredirect=true)
理由は、ファンクションアプリがファイルを参照しているためです。
組織を削除する際、特定の列自体を削除する必要があります。中身だけを削除するのではありません。
組織を追加する際、リストの最後に情報を追加する必要があります。

### 2-4.先々月分の本計上ファイル作成
「**毎月1日の9時**」に受け取る通知の指示に従ってください。
通知のタイトル: 「[AWS: 先々月分の本計上ファイル作成に関するお知らせ](https://teams.microsoft.com/l/channel/19%3a603300a3bef847d6ab3cfb7073c658c7%40thread.skype/%25E3%2581%258A%25E7%259F%25A5%25E3%2582%2589%25E3%2581%259B%2520-%2520%2520%25E3%2583%25AA%25E3%2582%25BB%25E3%2583%25BC%25E3%2583%25AB%25E8%25B3%2587%25E6%2596%2599%25E3%2581%25AB%25E9%2596%25A2%25E3%2581%2599%25E3%2582%258B%25E9%2580%259A%25E7%259F%25A5?groupId=8fb541f5-c8fd-457f-b38d-d81a2f21182c&tenantId=f8830191-2d31-48a8-881a-3060cbc873af)」
#### 作業手順
1. 「AWS/Billing/請求書」に移動してください。
2. 請求期間が先々月分であることを確認し、「すべてをcsvにダウンロード」を押下してください。
3. 「TeamKuramane/.../07_202108以降の事務処理/YYYYMM月度AWS計上資料」にcsvファイルをアップロードしてください。
4. csvファイルをxlsxファイルとして編集し、アップロードしてください。編集内容は以下の通りです。
- ファイル名 : ecsv_M_YYYY_本計上_月後.xlsx
（例：ecsv_9_2023_本計上_月後.xlsx）
- AD列1行目 : 「ExchangeRate」
- AD列2行目~AD列最終行 : 「AWS/Billing/請求書 」で確認した為替レートを入力
* 対象セルを全選択し、値入力後、「ctr + Enter」で自動入力可能です。
> 為替レートを追加する際は、以下の画像を参照してください
> <img width="387" alt="スクリーンショット 2023-10-19 16.12.20.png (97.5 kB)" src="https://files.esa.io/uploads/production/attachments/13068/2023/10/19/155118/5fcb6b0e-7159-4749-8fa1-757618789940.png">
5. 「[先々月分の本計上ファイル作成開始](https://auto-resale-system-fa.azurewebsites.net/api/awsrecordsforinvoices2monthago)  」を押下してください。
* 押下後、デフォルトのブラウザが開きます。
* 表示されない場合、エラーが発生しております。似里にご連絡ください。
6. 約1分後、ブラウザ上で「Executed/Success in: HTTP triggered function:AWSRecordsForInvoices2MonthAgo」の表示を確認してください。
7. 「TeamKuramane/.../07_202108以降の事務処理/YYYMM/YYYYMM月度AWS計上資料」 を確認してください。
8. 作成完了です。

> **警告**
> 新しいテナントを追加または既存のテナントを削除する際、以下の文書を修正する必要があります。[①SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_アカウント管理](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BAA322803-25D6-4119-9139-E1D50F7AEE5D%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E7%AE¡A7%BD%E7%90%86.xlsx&action=default&mobileredirect=true), 
[②SharePoint>TeamKuramane>SharedDocument>00_管理資料>AWSリセール>AWSリセール管理用_計上資料_基礎情報.xlsx](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BEFDFCF03-128F-4913-9065-B87B3CDFAB68%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE¡A7%BD%E7%90%86%E7%94%A8_%E8%A8¡A4%B8%8A%E8%B3%87%E6%96%99_%E5%9FºA4%8E%E6%83%85%E5%A0%B3.xlsx&action=default&mobileredirect=true)
理由は、ファンクションアプリがファイルを参照しているためです。
組織を削除する際、特定の列自体を削除する必要があります。中身だけを削除するのではありません。
組織を追加する際、リストの最後に情報を追加する必要があります。


# How to
## 環境構築
1. Azureアカウントの作成
2. 以下をインストール: Azure Functions Core Tools(ver. 4.0.4785 or later)( [MSのドキュメント](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cportal%2Cv2%2Cbash&pivots=programming-language-csharp#install-the-azure-functions-core-tools))
3. 以下をインストール:Python
4. 以下をインストール:Azure Functions extension for VS Code(ver. 1.8.1 or later) ([MSのドキュメント](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions))
5. (Optional 以下をインストール: Azurite V3 extension if you want to use a local storage emulator)
6. 以下を実行: $ pip install -r requirements.txt

## デプロイ時
1. ターミナルを開く
2. 以下を実行: $ func azure functionapp publish <APP_NAME>
[MSのドキュメント](https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-core-tools-reference?tabs=v2) about operation for function apps

## ソースコード
- Functions: [GitHub](https://github.com/Colorkrew/ParterCenter2Blob)
- Aleart: [Logic Apps](https://portal.azure.com/#@colorkrew.com/resource/subscriptions/316d2140-2429-4174-9103-5039e079fe54/resourceGroups/auto-resale-system/providers/Microsoft.Logic/workflows/aleart-from-auto-resale-system/logicApp)

## リソース
- Azure
    - Functions:
        - [AzureTenantFilesToSharePoint](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AzureTenantFilesToSharePoint): G02xxxxxx_BilledOneTimeInvoiceLineItems.csvを基に、AzureテナントのCSVファイルを作成します。
        - [AzureSubscriptionFilesToSharePoint](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AzureSubscriptionFilesToSharePoint): G02xxxxx_BilledOneTimeDailyRatedUsages.csvを基に、AzureサブスクリプションのCSVファイルを作成します。
        - [AzureTenantsAndSubscriptions](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AzureSummaryForTenantsAndSubscriptions): テナントとサブスクリプションの概要ファイルを作成します。
    - SharePoint:
        - [TeamKuramane>Shared Document>00_管理資料>事務関連>07-202108以降の事務処理>YYYYMM>Azure>Tenants](https://isaocorp.sharepoint.com/sites/TeamKuramane/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTeamKuramane%2FShared%20Documents%2F00%5F%E7%AE%A1%E7%90%86%E8%B3%87%E6%96%99%2F%E4%BA%8B%E5%8B%99%E9%96%A2%E9%80%A3%2F07%5F202108%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%8B%E5%8B%99%E5%87%A6%E7%90%86&viewid=653b928c%2D0d06%2D40e7%2Dbf0e%2Dd9e77774c9d3) :テナント毎のcsvファイルを保存
        - [TeamKuramane>Shared Document>00_管理資料>事務関連>07-202108以降の事務処理>YYYYMM>Azure>Subscriptions](https://isaocorp.sharepoint.com/sites/TeamKuramane/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTeamKuramane%2FShared%20Documents%2F00%5F%E7%AE%A1%E7%90%86%E8%B3%87%E6%96%99%2F%E4%BA%8B%E5%8B%99%E9%96%A2%E9%80%A3%2F07%5F202108%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%8B%E5%8B%99%E5%87%A6%E7%90%86&viewid=653b928c%2D0d06%2D40e7%2Dbf0e%2Dd9e77774c9d3) :サブスクリプション毎のcsvファイルを保存
        - [TeamKuramane>Shared Document>00_管理資料>事務関連>07-202108以降の事務処理>YYYYMM>Azure](https://isaocorp.sharepoint.com/sites/TeamKuramane/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTeamKuramane%2FShared%20Documents%2F00%5F%E7%AE%A1%E7%90%86%E8%B3%87%E6%96%99%2F%E4%BA%8B%E5%8B%99%E9%96%A2%E9%80%A3%2F07%5F202108%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%8B%E5%8B%99%E5%87%A6%E7%90%86&viewid=653b928c%2D0d06%2D40e7%2Dbf0e%2Dd9e77774c9d3) :テナントとサブスクリプション用の元データとサマリーファイルを格納

- AWS
    - [Cost Explorer](https://us-east-1.console.aws.amazon.com/cost-management/home?region=ap-northeast-1#/cost-explorer?chartStyle=STACK&costAggregate=unBlendedCost&endDate=2023-08-31&excludeForecasting=false&filter=%5B%5D&futureRelativeRange=CUSTOM&granularity=Monthly&groupBy=%5B%22Service%22%5D&historicalRelativeRange=LAST_6_MONTHS&isDefault=true&reportName=%E6%96%B0%E3%81%84%E3%82%B3%E3%82%B9%E3%83%88%E3%81%A8%E4%BD%BF%E7%94%A8%E7%8A%B6%E6%B3%81%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88&showOnlyUncategorized=false&showOnlyUntagged=false&startDate=2023-03-01&usageAggregate=undefined&useNormalizedUnits=false): 各テナントの費用請求に関するデータを保存および管理します。
    - [Lambda/AwsBilling](https://ap-northeast-1.console.aws.amazon.com/lambda/home?region=ap-northeast-1#/functions/AwsBilling?tab=code): 費用請求に関するデータを取得し、CSVファイルをS3にアップロードします。
    - [S3/awsbilling-colorkrew-s3](https://s3.console.aws.amazon.com/s3/buckets/awsbilling-colorkrew-s3?region=ap-northeast-1&tab=objects): 費用請求に関するCSVファイルを保存します。
    - Functions
        - [AWSS3ToSharePoint](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AzureSummaryForTenantsAndSubscriptions): 各企業に送信するためのPDFとして請求ファイルを作成します。
        - AWSRecordsForInvoices: 各月のECSVファイルに基づいて3か月分の記録を作成します。
            - [AWSRecordsForInvoices0MonthAgo](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AWSRecordsForInvoices0MonthAgo): 今月分の仮計上ファイルを作成
            - [AWSRecordsForinvoices1MonthAgo](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AWSRecordsForInvoices1MonthAgo): 先月分の仮計上ファイルを作成
            - [AWSRecordsForInvoices2MonthAgo](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Web/sites/auto-resale-system-fa/functions/AWSRecordsForInvoices2MonthAgo): 先々月分の本計上ファイルを作成。
    - SharePoint: 
        - [TeamKuramane>Shared Document>00_管理資料>事務関連>07-202108以降の事務処理>YYYYMM>YYYYMM-1月度AWS](https://isaocorp.sharepoint.com/sites/TeamKuramane/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTeamKuramane%2FShared%20Documents%2F00%5F%E7%AE%A1%E7%90%86%E8%B3%87%E6%96%99%2F%E4%BA%8B%E5%8B%99%E9%96%A2%E9%80%A3%2F07%5F202108%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%8B%E5%8B%99%E5%87%A6%E7%90%86&viewid=653b928c%2D0d06%2D40e7%2Dbf0e%2Dd9e77774c9d3):各社に送る用の請求書pdfファイルを保存します。
        - [TeamKuramane>Shared Document>00_管理資料>事務関連>07-202108以降の事務処理>YYYYMM>YYYYMM月度AWS](https://isaocorp.sharepoint.com/sites/TeamKuramane/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTeamKuramane%2FShared%20Documents%2F00%5F%E7%AE%A1%E7%90%86%E8%B3%87%E6%96%99%2F%E4%BA%8B%E5%8B%99%E9%96%A2%E9%80%A3%2F07%5F202108%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%8B%E5%8B%99%E5%87%A6%E7%90%86&viewid=653b928c%2D0d06%2D40e7%2Dbf0e%2Dd9e77774c9d3)計上資料とその元データファイルを保存します。
        - [AWSリセール管理用_アカウント管理.xlsx](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BAA322803-25D6-4119-9139-E1D50F7AEE5D%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE%A1%E7%90%86%E7%94%A8_%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E7%AE%A1%E7%90%86.xlsx&action=default&mobileredirect=true): アカウントに関する情報を記載。AWSS3ToSharePointで参照
        - [AWSリセール管理_計上資料_基礎情報.xlsx](https://isaocorp.sharepoint.com/:x:/r/sites/TeamKuramane/_layouts/15/Doc.aspx?sourcedoc=%7BEFDFCF03-128F-4913-9065-B87B3CDFAB68%7D&file=AWS%E3%83%AA%E3%82%BB%E3%83%BC%E3%83%AB%E7%AE%A1%E7%90%86%E7%94%A8_%E8%A8%88%E4%B8%8A%E8%B3%87%E6%96%99_%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1.xlsx&action=default&mobileredirect=true): アカウント毎の計上データについて記載。AWSRecordsForInvoicesにて参照
- トリガーツール
    - [trigger-functions-app-la](/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.Logic/workflows/trigger-functions-app-la): チームに通知を送信し、関数アプリをトリガーします。
- [auto-resale-system/auto-resale-system](https://portal.azure.com/#@colorkrew.com/resource/subscriptions/066e4d80-c150-4ee4-a893-b2f433717287/resourceGroups/auto-resale-system/providers/Microsoft.KeyVault/vaults/auto-resale-system/secrets): Functions AppとSharePointのシークレットを保存します 


## API
- Functions to SharePoint: [Office365-Rest-Python-Client.ClientCredentials](https://pypi.org/project/Office365-REST-Python-Client/)

## 計算方法
- Azure
    - 請求金額(税抜)
        - 従量課金の合計: Σ(EffectivePrice * units * ExchangeRate * 1/0.85)
        - Resarved Instancesの合計: Σ(EffectivePrice * units * ExchangeRate * 1.05)
        - Market Placeの合計: Σ( EffectivePrice * units * ExchangeRate * 1.08)
        - Licenseの合計: Σ( EffectivePrice * units * ExchangeRate * 1.08)
    - 請求金額(税込): Invoice = (Sum of Usages + Sum of Reserved Instances + Sum of License) * tax + Sum of Market Place
    - >Azure料金の計算方法として1.元データとしてSubtotalを用いる方法、2.EffectivePrice * units * ExchangeRateを用いる方法がある。MSの請求金額は1.Subtotalを元に算出している。しかしsubscriptionに関してはsubtotalの項目が無く、2.EffectivePrice * units(billiableQuantities) * ExchangeRateを使うしかない。
    - >問題点: 正の計算方法とは何か
対応策: effectiveUnitPlice * billiableQuantity * PCToBCExchangeRateを用いた計算方法を採用(2023/10/19)
比較する数値:
subtotalを用いた計算結果(colorkrewにおける計算方法)
SharePoint上の明細(おそらくbplatsによる計算を元にしたもの)
MSからの請求=subtotalの合計
subtotalの合計=GXXXXXXX_BilledOneTimeInvoiceLineItemsのsubtotalの合計
subtotalの合計≠SharePoint上の明細 
SharePoint上の明細=effectiveUnitPlice * billiableQuantity * PCToBCExchangeRate
subtotal ≒effectiveUnitPlice * billiableQuantity * PCToBCExchangeRate
備考:
本来であればsubtotalとeffectiveUnitPlice * billiableQuantity * PCToBCExchangeRateの整数表記は合致すべき。だが実際に数円の誤差があり、それにより計算結果の誤差が生じる可能性がある。
- AWS
    - 請求金額合計(税抜): Sum of Resources =  Σ(Amount) *月中平均TTS レート(三菱UFJ銀行より) * 1.1
    -  日本国土開発株式会社のみ手数料は1,000円(経緯不明)


# Dependencies
- [Quick start for Azure Functions in VS Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)
- [Python for Azure Blob](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli)
- [Homebrew](https://brew.sh/)
- requirements.txt
    - azure-functions==1.17.0
    - azure-identity==1.14.0
    - azure-storage-blob==12.17.0
    - python-dotenv==1.0.0
    - Office365-REST-Python-Client==2.4.3
    - boto3==1.28.38
    - reportlab==4.0.4
    - bs4==0.0.1
    - openpyxl==3.1.2
- The following requirements were added by pip freeze:
    - azure-core==1.29.3
    - beautifulsoup4==4.12.2
    - botocore==1.31.38
    - certifi==2023.7.22
    - cffi==1.15.1
    - charset-normalizer==3.2.0
    - cryptography==41.0.3
    - et-xmlfile==1.1.0
    - idna==3.4
    - isodate==0.6.1
    - jmespath==1.0.1
    - msal==1.23.0
    - msal-extensions==1.0.0
    - Pillow==10.0.0
    - portalocker==2.7.0
    - pycparser==2.21
    - PyJWT==2.8.0
    - python-dateutil==2.8.2
    - pytz==2023.3
    - requests==2.31.0
    - s3transfer==0.6.2
    - six==1.16.0
    - soupsieve==2.5
    - typing_extensions==4.7.1
    - urllib3==1.26.16




