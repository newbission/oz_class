from django.contrib import admin
from .models import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    # 리스트에 표시할 정보
    list_display = ("title", "writer", "content", "likes", "date", "created_at", "updated_at")

    # 필터기능
    list_filter = ("date", "writer")
    
    # 검색 기능
    search_fields = ("title", "content")

    # 기본정렬
    ordering = ("-date",) # -: 역순

    # 읽기전용필드(수정불가)
    readonly_fields = ("writer",)

    # 상세페이지 필드 분리
    fieldsets = (
        (None, {"fields": ("title", "content")}),
        ("Advanced options", # "Advanced options" : 원하는 필드명으로 수정 가능
            {
                "fields": ("writer", "likes", "reviews"),
                "classes": ("collapse")
            }
        )
    )

    list_per_page: 10

    # 사용자 정의 작업 추가
    actions = ("increment_likes",) 
    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = "선택된 게시글의 좋아요 수 1 증가"