# create table AISystem_Category_Media
# (
#     Id         int identity
#         constraint PK_AISystem_Category_Media
#             primary key,
#     UnitCode   nvarchar(50),
#     ParentId   int,
#     Title      nvarchar(250),
#     Code       nvarchar(50),
#     Status     int,
#     OrderNo    int,
#     PortalId   int,
#     LanguageId nvarchar(50),
#     ChildId    nvarchar(max)
# )