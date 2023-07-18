SELECT COALESCE(MAX(LastUpdated),'1900-01-01') as LastUpdated
FROM dppr_book.orders;
